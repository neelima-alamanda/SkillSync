import './FacultyDashboard.css'

const stats = [
  { label: 'Industry Internships', value: '18' },
  { label: 'FDP Programs', value: '7' },
  { label: 'Research Collaborations', value: '12' },
  { label: 'Workshops', value: '24' },
]

const opportunities = [
  {
    title: 'Faculty Industry Internship',
    organization: 'TechNova Solutions',
    type: 'Faculty Internship',
    date: '18 Sep 2026',
    status: 'Open',
  },
  {
    title: 'AI & Machine Learning FDP',
    organization: 'SkillSync Learning Hub',
    type: 'FDP',
    date: '25 Sep 2026',
    status: 'Open',
  },
  {
    title: 'Industry Research Collaboration',
    organization: 'InnovateX Labs',
    type: 'Research',
    date: '30 Sep 2026',
    status: 'Open',
  },
]

const activities = [
  {
    title: 'Applied AI Research Program',
    description: 'Collaboration opportunity with an industry research team.',
    tag: 'Research',
  },
  {
    title: 'Advanced React Workshop',
    description: 'Industry-led workshop for faculty members.',
    tag: 'Workshop',
  },
  {
    title: 'Industry Training Program',
    description: 'Hands-on industrial training opportunity.',
    tag: 'Training',
  },
]

function FacultyDashboard() {
  return (
    <div className="faculty-dashboard">
      <header className="faculty-header">
        <div>
          <p className="eyebrow">Faculty Portal</p>
          <h1>Welcome back, Faculty 👋</h1>
          <p className="header-description">
            Discover industry opportunities, professional development programs,
            and research collaborations from one place.
          </p>
        </div>

        <div className="header-actions">
          <button className="secondary-button">View Programs</button>
          <button className="primary-button">Explore Opportunities</button>
        </div>
      </header>

      <section className="faculty-stats-grid">
        {stats.map((stat) => (
          <div className="faculty-stat-card" key={stat.label}>
            <p>{stat.label}</p>
            <h2>{stat.value}</h2>
          </div>
        ))}
      </section>

      <section className="faculty-main-grid">
        <div className="faculty-section">
          <div className="section-heading">
            <div>
              <p className="eyebrow">Industry & Academia</p>
              <h2>Upcoming Opportunities</h2>
            </div>
            <button className="text-button">View All</button>
          </div>

          <div className="opportunity-list">
            {opportunities.map((opportunity) => (
              <div className="faculty-opportunity-row" key={opportunity.title}>
                <div className="opportunity-icon">
                  {opportunity.type.charAt(0)}
                </div>

                <div className="opportunity-info">
                  <h3>{opportunity.title}</h3>
                  <p>{opportunity.organization}</p>

                  <div className="opportunity-meta">
                    <span>{opportunity.type}</span>
                    <span>Deadline: {opportunity.date}</span>
                  </div>
                </div>

                <span className="open-badge">{opportunity.status}</span>
              </div>
            ))}
          </div>
        </div>

        <div className="faculty-section quick-actions">
          <div className="section-heading">
            <div>
              <p className="eyebrow">Faculty Tools</p>
              <h2>Quick Actions</h2>
            </div>
          </div>

          <button className="faculty-action-card">
            <strong>Find Internship</strong>
            <span>Explore industry internship opportunities</span>
          </button>

          <button className="faculty-action-card">
            <strong>Apply for FDP</strong>
            <span>Join professional development programs</span>
          </button>

          <button className="faculty-action-card">
            <strong>Research Collaboration</strong>
            <span>Connect with industry research teams</span>
          </button>

          <button className="faculty-action-card">
            <strong>View Workshops</strong>
            <span>Discover upcoming technical workshops</span>
          </button>
        </div>
      </section>

      <section className="faculty-section activity-section">
        <div className="section-heading">
          <div>
            <p className="eyebrow">Professional Development</p>
            <h2>Featured Programs</h2>
          </div>
          <button className="text-button">Explore More</button>
        </div>

        <div className="activity-grid">
          {activities.map((activity) => (
            <div className="activity-card" key={activity.title}>
              <span className="activity-tag">{activity.tag}</span>

              <h3>{activity.title}</h3>

              <p>{activity.description}</p>

              <button className="learn-button">View Details →</button>
            </div>
          ))}
        </div>
      </section>
    </div>
  )
}

export default FacultyDashboard