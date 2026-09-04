const opportunity = {
  title: 'Python Developer',
  organization: 'TechNova',
  type: 'Full-time',
  location: 'Hyderabad',
  match: '90%',
  description:
    'Develop backend applications using Python and Flask while working with relational databases.',
  requiredSkills: ['Python', 'Flask', 'SQL'],
}

function OpportunityDetails() {
  return (
    <main>
      <header>
        <h1>{opportunity.title}</h1>
        <p>{opportunity.organization}</p>
      </header>

      <section>
        <h2>Opportunity Details</h2>

        <p>
          <strong>Type:</strong> {opportunity.type}
        </p>

        <p>
          <strong>Location:</strong> {opportunity.location}
        </p>

        <p>
          <strong>Skill Match:</strong> {opportunity.match}
        </p>

        <p>{opportunity.description}</p>
      </section>

      <section>
        <h2>Required Skills</h2>

        <ul>
          {opportunity.requiredSkills.map((skill) => (
            <li key={skill}>{skill}</li>
          ))}
        </ul>
      </section>

      <button type="button">Apply Now</button>
    </main>
  )
}

export default OpportunityDetails