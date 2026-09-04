import './RecruiterDashboard.css'

const stats = [
  { label: 'Active Jobs', value: '12' },
  { label: 'Active Internships', value: '8' },
  { label: 'Applications', value: '126' },
  { label: 'Shortlisted', value: '24' },
]

const recentApplications = [
  {
    name: 'Ananya Reddy',
    role: 'Frontend Developer Intern',
    skills: 'React, JavaScript',
    status: 'Shortlisted',
  },
  {
    name: 'Rahul Kumar',
    role: 'Python Developer',
    skills: 'Python, Flask',
    status: 'Under Review',
  },
  {
    name: 'Sneha Patel',
    role: 'Data Analyst Intern',
    skills: 'Python, SQL',
    status: 'Shortlisted',
  },
  {
    name: 'Arjun Rao',
    role: 'Backend Developer',
    skills: 'Flask, SQLAlchemy',
    status: 'New',
  },
]

const opportunities = [
  {
    title: 'Frontend Developer Intern',
    type: 'Internship',
    applications: 38,
    deadline: '20 Sep 2026',
  },
  {
    title: 'Python Backend Developer',
    type: 'Job',
    applications: 54,
    deadline: '28 Sep 2026',
  },
  {
    title: 'Data Analytics Internship',
    type: 'Internship',
    applications: 34,
    deadline: '05 Oct 2026',
  },
]

function RecruiterDashboard() {
  return (
    <div className="recruiter-dashboard">
      <header className="dashboard-header">
        <div>
          <p className="eyebrow">Recruiter Portal</p>
          <h1>Welcome back, Recruiter 👋</h1>
          <p className="header-description">
            Manage your opportunities, applications, and candidate pipeline
            from one place.
          </p>
        </div>

        <div className="header-actions">
          <button className="secondary-button">View Applications</button>
          <button className="primary-button">+ Post Opportunity</button>
        </div>
      </header>

      <section className="stats-grid">
        {stats.map((stat) => (
          <div className="stat-card" key={stat.label}>
            <p>{stat.label}</p>
            <h2>{stat.value}</h2>
          </div>
        ))}
      </section>

      <section className="dashboard-grid">
        <div className="dashboard-section applications-section">
          <div className="section-heading">
            <div>
              <p className="eyebrow">Candidate Pipeline</p>
              <h2>Recent Applications</h2>
            </div>
            <button className="text-button">View All</button>
          </div>

          <div className="applications-list">
            {recentApplications.map((application) => (
              <div className="application-row" key={application.name}>
                <div className="candidate-avatar">
                  {application.name.charAt(0)}
                </div>

                <div className="candidate-info">
                  <h3>{application.name}</h3>
                  <p>{application.role}</p>
                  <span>{application.skills}</span>
                </div>

                <span
                  className={`status-badge ${application.status
                    .toLowerCase()
                    .replace(' ', '-')}`}
                >
                  {application.status}
                </span>
              </div>
            ))}
          </div>
        </div>

        <div className="dashboard-section quick-actions">
          <div className="section-heading">
            <div>
              <p className="eyebrow">Recruitment Tools</p>
              <h2>Quick Actions</h2>
            </div>
          </div>

          <button className="action-card">
            <strong>Post a Job</strong>
            <span>Create a new industry job opening</span>
          </button>

          <button className="action-card">
            <strong>Post an Internship</strong>
            <span>Find students for internship roles</span>
          </button>

          <button className="action-card">
            <strong>Review Candidates</strong>
            <span>Evaluate and shortlist applicants</span>
          </button>
        </div>
      </section>

      <section className="dashboard-section opportunities-section">
        <div className="section-heading">
          <div>
            <p className="eyebrow">Your Listings</p>
            <h2>Active Opportunities</h2>
          </div>
          <button className="text-button">Manage All</button>
        </div>

        <div className="opportunities-grid">
          {opportunities.map((opportunity) => (
            <div className="opportunity-card" key={opportunity.title}>
              <div className="opportunity-top">
                <span className="opportunity-type">{opportunity.type}</span>
                <span className="active-dot">Active</span>
              </div>

              <h3>{opportunity.title}</h3>

              <div className="opportunity-details">
                <span>{opportunity.applications} applications</span>
                <span>Deadline: {opportunity.deadline}</span>
              </div>

              <button className="manage-button">Manage Opportunity</button>
            </div>
          ))}
        </div>
      </section>
    </div>
  )
}

export default RecruiterDashboard

