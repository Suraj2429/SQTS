from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from .database import engine, SessionLocal
from .models import Base, Lead, ChatLog, FAQ
from .ai_service import get_ai_response
from .recommendations import career_recommendations
from .session_manager import conversation_state

Base.metadata.create_all(bind=engine)

app=FastAPI(
    title="Career Guidance Bot"
)

app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )

@app.get("/chat")
def chat(query: str):
    user_message = query.lower().strip()

    # Reset conversation

    if user_message in [
        "reset",
        "cancel",
        "new chat",
        "start over"
    ]:

        conversation_state.clear()

        return {
            "response":
            "Conversation reset successfully. How can I help you today?"
        }

    # Continue Lead Flow

    if conversation_state.get("step") == "education":

        conversation_state["education"] = query
        conversation_state["step"] = "skill"

        return {
            "response":
            "What is your skill level? (Beginner / Intermediate / Advanced)"
        }

    if conversation_state.get("step") == "skill":

        conversation_state["skill"] = query
        conversation_state["step"] = "name"

        return {
            "response":
            "Please enter your full name."
        }

    if conversation_state.get("step") == "name":

        conversation_state["name"] = query
        conversation_state["step"] = "email"

        return {
            "response":
            "Please enter your email."
        }

    if conversation_state.get("step") == "email":

        conversation_state["email"] = query

        db = SessionLocal()

        lead = Lead(
            name=conversation_state["name"],
            email=conversation_state["email"],
            education=conversation_state["education"],
            skills=conversation_state["skill"],
            interest=conversation_state["interest"]
        )

        db.add(lead)

        log = ChatLog(
            question=conversation_state["interest"],
            response="Roadmap Generated"
        )

        db.add(log)

        db.commit()
        db.close()

        interest = conversation_state["interest"]
        skill = conversation_state["skill"].lower()

        if interest == "Python":

            if skill == "beginner":
                roadmap = career_recommendations["python_beginner"]

            elif skill == "intermediate":
                roadmap = career_recommendations["python_intermediate"]

            else:
                roadmap = career_recommendations["python_advanced"]

        elif interest == "Java":

            roadmap = career_recommendations["java"]

        elif interest == "Data Analytics":

            roadmap = career_recommendations["data_analytics"]

        elif interest == "Web Development":

            roadmap = career_recommendations["web_development"]

        else:

            roadmap = "Roadmap not available."

        conversation_state.clear()

        return {
            "response":
            "Lead saved successfully.\n\n" + roadmap
        }

    # Start Lead Flow ONLY from Buttons

    domains = {
        "python": "Python",
        "java": "Java",
        "data analytics": "Data Analytics",
        "web development": "Web Development"
    }

    if user_message in domains:

        conversation_state.clear()

        conversation_state["interest"] = domains[user_message]
        conversation_state["step"] = "education"

        return {
            "response":
            f"You selected {domains[user_message]}.\n\n"
            "What is your education? (BCA / MCA / BTech / Other)"
        }

    # FAQ Search

    db = SessionLocal()

    faqs = db.query(FAQ).all()

    for faq in faqs:

        if (
            faq.question.lower() in user_message
            or
            user_message in faq.question.lower()
        ):

            db.close()

            return {
                "response": faq.answer
            }

    db.close()

    # AI Fallback
    ai_response = get_ai_response(query)

    return {
        "response": ai_response
    }

 
@app.get("/leads")
def get_leads():

    db = SessionLocal()

    leads = db.query(Lead).all()

    data = []

    for lead in leads:

        data.append({
            "id":lead.id,
            "name":lead.name,
            "email":lead.email,
            "education":lead.education,
            "skills":lead.skills,
            "interest":lead.interest
        })

    db.close()

    return data

@app.get("/analytics")
def analytics():

    db=SessionLocal()

    total_leads=db.query(Lead).count()

    total_chats=db.query(ChatLog).count()

    success_ratio=0

    if total_chats>0:

        success_ratio=round(
            (total_leads/total_chats)*100,
            2
        )

    db.close()

    return {
        "total_leads":total_leads,
        "total_chats":total_chats,
        "chat_success_ratio":f"{success_ratio}%"
    }

@app.get("/admin", response_class=HTMLResponse)
def admin():

    db = SessionLocal()

    leads = db.query(Lead).all()

    total_leads = db.query(Lead).count()

    total_chats = db.query(ChatLog).count()

    logs = db.query(ChatLog).all()

    topic_count = {}

    for log in logs:

        topic_count[log.question] = (
            topic_count.get(log.question,0) + 1
        )

    most_asked = "No Data"

    if topic_count:

        most_asked = max(
            topic_count,
            key=topic_count.get
        )

    success_ratio = 0

    if total_chats > 0:
        success_ratio = round(
            (total_leads / total_chats) * 100,
            2
        )

    html = f"""
    <html>
    <head>
        <title>Career Guidance Dashboard</title>

        <style>

        body{{
            font-family:Arial,sans-serif;
            background:#f4f6f9;
            padding:30px;
        }}

        h1{{
            color:#2563eb;
        }}

        .cards{{
            display:flex;
            gap:20px;
            margin-bottom:30px;
        }}

        .card{{
            background:white;
            padding:20px;
            border-radius:12px;
            box-shadow:0 2px 10px rgba(0,0,0,0.1);
            min-width:220px;
        }}

        .card h2{{
            margin:0;
            color:#2563eb;
        }}

        table{{
            width:100%;
            border-collapse:collapse;
            background:white;
            border-radius:12px;
            overflow:hidden;
            box-shadow:0 2px 10px rgba(0,0,0,0.1);
        }}

        th{{
            background:#2563eb;
            color:white;
            padding:14px;
        }}

        td{{
            padding:12px;
            border-bottom:1px solid #eee;
        }}

        tr:hover{{
            background:#f8fafc;
        }}

        </style>

    </head>

    <body>

    <h1>Career Guidance Dashboard</h1>

    <div class="cards">

        <div class="card">
            <h2>{total_leads}</h2>
            <p>Total Leads</p>
        </div>

        <div class="card">
            <h2>{total_chats}</h2>
            <p>Total Chats</p>
        </div>

        <div class="card">
            <h2>{success_ratio}%</h2>
            <p>Success Ratio</p>
        </div>

        <div class="card">
            <h2>{most_asked}</h2>
            <p>Most Asked Topic</p>
        </div>

    </div>

    <table>

        <tr>
            <th>ID</th>
            <th>Name</th>
            <th>Email</th>
            <th>Education</th>
            <th>Skills</th>
            <th>Interest</th>
        </tr>
    """

    for lead in leads:

        html += f"""
        <tr>
            <td>{lead.id}</td>
            <td>{lead.name}</td>
            <td>{lead.email}</td>
            <td>{lead.education}</td>
            <td>{lead.skills}</td>
            <td>{lead.interest}</td>
        </tr>
        """

    html += """
    </table>

    </body>
    </html>
    """

    db.close()

    return HTMLResponse(content=html)