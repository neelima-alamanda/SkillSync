const recommendations = [
  {
    id: 1,
    title: 'Frontend Developer Intern',
    organization: 'Tech Solutions',
    type: 'Internship',
    match: '92%',
    skills: ['React', 'JavaScript', 'Git'],
  },
  {
    id: 2,
    title: 'Python Developer',
    organization: 'DataWorks',
    type: 'Job',
    match: '86%',
    skills: ['Python', 'SQL', 'Git'],
  },
  {
    id: 3,
    title: 'Full Stack Development Program',
    organization: 'Innovation Labs',
    type: 'Program',
    match: '81%',
    skills: ['React', 'Python', 'SQL'],
  },
]

function RecommendationFeed() {
  return (
    <section>
      <h2>Recommended Opportunities</h2>
      <p>
        Explore opportunities that match your skills and career interests.
      </p>

      {recommendations.map((recommendation) => (
        <article key={recommendation.id}>
          <h3>{recommendation.title}</h3>

          <p>{recommendation.organization}</p>
          <p>{recommendation.type}</p>
          <p>Skill Match: {recommendation.match}</p>

          <div>
            <strong>Relevant Skills:</strong>

            <ul>
              {recommendation.skills.map((skill) => (
                <li key={skill}>{skill}</li>
              ))}
            </ul>
          </div>

          <button type="button">
            View Opportunity
          </button>
        </article>
      ))}
    </section>
  )
}

export default RecommendationFeed