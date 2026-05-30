from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session

from .ai_service import get_ai_response
from .database import engine, SessionLocal
from .models import Base, FAQ, Lead

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="AI Career Guidance Chatbot"
)

app.mount(
    "/static",
    StaticFiles(directory="app/static"),
    name="static"
)

templates = Jinja2Templates(
    directory="app/templates"
)


@app.get("/", response_class=HTMLResponse)
async def home(request: Request):

    return templates.TemplateResponse(
        request=request,
        name="index.html"
    )


@app.get("/chat")
async def chat(query: str):

    db: Session = SessionLocal()

    user_message = query.lower().strip()

    faqs = db.query(FAQ).all()

    for faq in faqs:

        if faq.question.lower() in user_message:

            db.close()

            return {
                "response": faq.answer
            }

    db.close()

    ai_response = get_ai_response(query)

    return {
        "response": ai_response
    }


@app.post("/submit-lead")
async def submit_lead(

    name: str = Form(...),
    email: str = Form(...),
    interest: str = Form(...)

):

    db: Session = SessionLocal()

    new_lead = Lead(
        name=name,
        email=email,
        interest=interest
    )

    db.add(new_lead)

    db.commit()

    db.close()

    return {
        "message": "Lead submitted successfully"
    }


@app.get("/admin/leads")
async def get_leads():

    db: Session = SessionLocal()

    leads = db.query(Lead).all()

    data = []

    for lead in leads:

        data.append({
            "id": lead.id,
            "name": lead.name,
            "email": lead.email,
            "interest": lead.interest
        })

    db.close()

    return data


@app.get("/admin", response_class=HTMLResponse)
async def admin_panel():

    db: Session = SessionLocal()

    leads = db.query(Lead).all()

    total_leads = len(leads)

    html = f"""

    <html>

    <head>

        <title>Admin Dashboard</title>

        <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>

        <style>

            *{{
                margin:0;
                padding:0;
                box-sizing:border-box;
            }}

            body{{
                font-family:Arial,sans-serif;
                background:#f4f7fb;
                padding:30px;
            }}

            h1{{
                margin-bottom:25px;
                color:#111827;
            }}

            .dashboard{{
                display:flex;
                gap:20px;
                margin-bottom:30px;
                flex-wrap:wrap;
            }}

            .card{{
                flex:1;
                min-width:220px;
                background:white;
                padding:25px;
                border-radius:15px;
                box-shadow:0 5px 15px rgba(0,0,0,0.08);
            }}

            .card h2{{
                font-size:32px;
                color:#2563eb;
                margin-bottom:10px;
            }}

            .card p{{
                color:#555;
                font-size:16px;
            }}

            .form-container{{
                background:white;
                padding:25px;
                border-radius:15px;
                margin-bottom:30px;
                box-shadow:0 5px 15px rgba(0,0,0,0.08);
            }}

            .form-container h2{{
                margin-bottom:20px;
                color:#111827;
            }}

            .form-container form{{
                display:flex;
                flex-direction:column;
                gap:18px;
            }}

            .form-group{{
                display:flex;
                flex-direction:column;
            }}

            .form-group label{{
                margin-bottom:8px;
                font-weight:bold;
                color:#374151;
            }}

            .form-group input,
            .form-group textarea{{
                width:100%;
                padding:14px;
                border:1px solid #d1d5db;
                border-radius:12px;
                font-size:15px;
                outline:none;
            }}

            .form-group textarea{{
                min-height:120px;
                resize:vertical;
            }}

            .form-group input:focus,
            .form-group textarea:focus{{
                border-color:#2563eb;
            }}

            .form-container button{{
                padding:14px;
                border:none;
                background:#2563eb;
                color:white;
                border-radius:12px;
                font-size:16px;
                cursor:pointer;
            }}

            .form-container button:hover{{
                background:#1d4ed8;
            }}

            .table-container{{
                background:white;
                padding:20px;
                border-radius:15px;
                box-shadow:0 5px 15px rgba(0,0,0,0.08);
                overflow-x:auto;
            }}

            table{{
                width:100%;
                border-collapse:collapse;
            }}

            th{{
                background:#2563eb;
                color:white;
                padding:14px;
                text-align:left;
            }}

            td{{
                padding:14px;
                border-bottom:1px solid #ddd;
            }}

            tr:hover{{
                background:#f1f5f9;
            }}

            .chart-container{{
                margin-top:30px;
                background:white;
                padding:20px;
                border-radius:15px;
                box-shadow:0 5px 15px rgba(0,0,0,0.08);
            }}

            @media(max-width:768px){{

                body{{
                    padding:15px;
                }}

                .dashboard{{
                    flex-direction:column;
                }}

            }}

        </style>

    </head>

    <body>

        <h1>Lead Dashboard</h1>

        <div class="dashboard">

            <div class="card">
                <h2>{total_leads}</h2>
                <p>Total Leads</p>
            </div>

            <div class="card">
                <h2>4</h2>
                <p>Popular Courses</p>
            </div>

            <div class="card">
                <h2>24</h2>
                <p>Total Queries</p>
            </div>

        </div>

        <div class="form-container">

            <h2>Add FAQ</h2>

            <form method="post" action="/add-faq">

                <div class="form-group">

                    <label>Question</label>

                    <input
                        type="text"
                        name="question"
                        placeholder="Enter question"
                        required
                    >

                </div>

                <div class="form-group">

                    <label>Answer</label>

                    <textarea
                        name="answer"
                        placeholder="Enter answer"
                        required
                    ></textarea>

                </div>

                <button type="submit">
                    Add FAQ
                </button>

            </form>

        </div>

        <div class="table-container">

            <table>

                <tr>
                    <th>ID</th>
                    <th>Name</th>
                    <th>Email</th>
                    <th>Interest</th>
                </tr>

    """

    for lead in leads:

        html += f"""

                <tr>
                    <td>{lead.id}</td>
                    <td>{lead.name}</td>
                    <td>{lead.email}</td>
                    <td>{lead.interest}</td>
                </tr>

        """

    html += """

            </table>

        </div>

        <div class="chart-container">

            <canvas id="leadChart"></canvas>

        </div>

        <script>

            const ctx = document.getElementById('leadChart');

            new Chart(ctx, {

                type:'bar',

                data:{

                    labels:['Python','Web','AI','DevOps'],

                    datasets:[{

                        label:'Student Interests',

                        data:[12,8,6,4],

                        borderWidth:1

                    }]
                },

                options:{

                    responsive:true,

                    scales:{
                        y:{
                            beginAtZero:true
                        }
                    }
                }
            });

        </script>

    </body>

    </html>

    """

    db.close()

    return html


@app.post("/add-faq")
async def add_faq(

    question: str = Form(...),
    answer: str = Form(...)

):

    db: Session = SessionLocal()

    faq = FAQ(
        question=question.lower(),
        answer=answer
    )

    db.add(faq)

    db.commit()

    db.close()

    return RedirectResponse(
        url="/admin",
        status_code=303
    )