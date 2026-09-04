import './AdminDashboard.css'

const stats = [
  { label: 'Total Students', value: '2,480' },
  { label: 'Faculty Members', value: '186' },
  { label: 'Industry Partners', value: '74' },
  { label: 'Active Opportunities', value: '142' },
]

const recentActivities = [
  {
    title: 'New Industry Partner Registered',
    description: 'TechNova Solutions joined the SkillSync platform.',
    type: 'Industry',
    time: '2 hours ago',
  },
  {
    title: 'Student Skill Assessment Completed',
    description: '42 students completed their latest skill assessments.',
    type: 'Students',
    time: '5 hours ago',
  },
  {
    title: 'New Internship Opportunities',
    description: '18 new internship opportunities were published.',
    type: 'Opportunities',
    time: 'Yesterday',
  },
  {
    title: 'Faculty Research Collaboration',
    description: 'A new research collaboration request was submitted.',
    type: 'Research',
    time: 'Yesterday',
  },
]

const managementActions = [
  {
    title: 'Manage Students',
    description: 'View and manage student profiles and skill records.',
  },
  {
    title: 'Manage Faculty',
    description: 'Review faculty profiles and professional activities.',
  },
  {
    title: 'Manage Industries',
    description: 'Manage industry partners and collaboration requests.',
  },
  {
    title: 'Manage Opportunities',
    description: 'Monitor jobs, internships, projects, and programs.',
  },
]

const analytics = [
  { label: 'Student Placement Rate', value: '82%' },
  { label: 'Industry Engagement', value: '76%' },
  { label: 'Skill Assessment Completion', value: '91%' },
]

function AdminDashboard() {
  return (
    <div className="admin-dashboard">
      <header className="admin-header">
        <div>
          <p className="eyebrow">Administration Portal</p>
          <h1>Welcome back, Admin 👋</h1>
          <p className="header-description">
            Monitor SkillSync activity, manage stakeholders, and track
            institution-wide career and industry engagement.
          </p>
        </div>

        <div className="admin-header-actions">
          <button className="secondary-button">View Reports</button>
          <button className="primary-button">Manage Platform</button>
        </div>
      </header>

      <section className="admin-stats-grid">
        {stats.map((stat) => (
          <div className="admin-stat-card" key={stat.label}>
            <p>{stat.label}</p>
            <h2>{stat.value}</h2>
          </div>
        ))}
      </section>

      <section className="admin-main-grid">
        <div className="admin-section">
          <div className="section-heading">
            <div>
              <p className="eyebrow">Platform Monitoring</p>
              <h2>Recent Activities</h2>
            </div>

            <button className="text-button">View All</button>
          </div>

          <div className="activity-list">
            {recentActivities.map((activity) => (
              <div className="admin-activity-row" key={activity.title}>
                <div className="activity-icon">
                  {activity.type.charAt(0)}
                </div>

                <div className="activity-info">
                  <h3>{activity.title}</h3>
                  <p>{activity.description}</p>
                  <span>{activity.time}</span>
                </div>

                <span className="activity-badge">{activity.type}</span>
              </div>
            ))}
          </div>
        </div>

        <div className="admin-section">
          <div className="section-heading">
            <div>
              <p className="eyebrow">Administration</p>
              <h2>Quick Management</h2>
            </div>
          </div>

          <div className="management-list">
            {managementActions.map((action) => (
              <button className="management-card" key={action.title}>
                <strong>{action.title}</strong>
                <span>{action.description}</span>
              </button>
            ))}
          </div>
        </div>
      </section>

      <section className="admin-section analytics-section">
        <div className="section-heading">
          <div>
            <p className="eyebrow">Institution Insights</p>
            <h2>Platform Analytics</h2>
          </div>

          <button className="text-button">Detailed Analytics</button>
        </div>

        <div className="analytics-grid">
          {analytics.map((item) => (
            <div className="analytics-card" key={item.label}>
              <p>{item.label}</p>
              <h3>{item.value}</h3>

              <div className="progress-track">
                <div
                  className="progress-fill"
                  style={{ width: item.value }}
                />
              </div>
            </div>
          ))}
        </div>
      </section>

      <section className="admin-section overview-section">
        <div className="section-heading">
          <div>
            <p className="eyebrow">Platform Overview</p>
            <h2>Admin Responsibilities</h2>
          </div>
        </div>

        <div className="overview-grid">
          <div className="overview-card">
            <h3>Student Development</h3>
            <p>
              Monitor student skill assessments, portfolios, certifications,
              internships, and placement readiness.
            </p>
          </div>

          <div className="overview-card">
            <h3>Industry Collaboration</h3>
            <p>
              Track industry partnerships, opportunities, mentorships,
              workshops, and live projects.
            </p>
          </div>

          <div className="overview-card">
            <h3>Faculty Engagement</h3>
            <p>
              Monitor faculty internships, FDPs, industrial training, research,
              and consultancy activities.
            </p>
          </div>
        </div>
      </section>
    </div>
  )
}

export default AdminDashboard