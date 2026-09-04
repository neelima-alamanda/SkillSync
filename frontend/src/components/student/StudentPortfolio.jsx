const portfolio = {
  name: 'Alex Student',
  headline: 'Computer Science Student | Aspiring Full Stack Developer',
  institution: 'ABC Institute of Technology',
  course: 'B.Tech Computer Science',
  graduationYear: '2027',
  skills: ['React', 'JavaScript', 'Python', 'SQL', 'Git'],
  projects: [
    {
      title: 'SkillSync',
      description: 'A platform connecting students with relevant career opportunities.',
      technologies: ['React', 'Python', 'SQL'],
    },
    {
      title: 'Student Management System',
      description: 'A web application for managing student academic information.',
      technologies: ['JavaScript', 'SQL'],
    },
  ],
  certifications: [
    'Introduction to Web Development',
    'Python Programming Fundamentals',
  ],
  achievements: [
    'Participated in Smart India Hackathon',
    'Completed 100+ coding challenges',
  ],
}

function StudentPortfolio() {
  return (
    <main>
      <header>
        <h1>{portfolio.name}</h1>
        <p>{portfolio.headline}</p>
        <p>{portfolio.institution}</p>
        <p>
          {portfolio.course} · Graduation: {portfolio.graduationYear}
        </p>
      </header>

      <section>
        <h2>Skills</h2>

        <ul>
          {portfolio.skills.map((skill) => (
            <li key={skill}>{skill}</li>
          ))}
        </ul>
      </section>

      <section>
        <h2>Projects</h2>

        {portfolio.projects.map((project) => (
          <article key={project.title}>
            <h3>{project.title}</h3>
            <p>{project.description}</p>

            <strong>Technologies:</strong>
            <ul>
              {project.technologies.map((technology) => (
                <li key={technology}>{technology}</li>
              ))}
            </ul>
          </article>
        ))}
      </section>

      <section>
        <h2>Certifications</h2>

        <ul>
          {portfolio.certifications.map((certification) => (
            <li key={certification}>{certification}</li>
          ))}
        </ul>
      </section>

      <section>
        <h2>Achievements</h2>

        <ul>
          {portfolio.achievements.map((achievement) => (
            <li key={achievement}>{achievement}</li>
          ))}
        </ul>
      </section>
    </main>
  )
}

export default StudentPortfolio