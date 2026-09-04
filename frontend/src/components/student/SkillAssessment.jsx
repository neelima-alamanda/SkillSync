import { useState } from 'react'

const skills = [
  'JavaScript',
  'React',
  'Python',
  'SQL',
  'Git',
]

function SkillAssessment() {
  const [ratings, setRatings] = useState({
    JavaScript: 0,
    React: 0,
    Python: 0,
    SQL: 0,
    Git: 0,
  })

  const handleRatingChange = (skill, rating) => {
    setRatings({
      ...ratings,
      [skill]: Number(rating),
    })
  }

  return (
    <section>
      <h2>Skill Assessment</h2>
      <p>
        Rate your current skill level from 1 (beginner) to 5 (advanced).
      </p>

      {skills.map((skill) => (
        <div key={skill}>
          <label htmlFor={skill}>{skill}</label>

          <select
            id={skill}
            value={ratings[skill]}
            onChange={(event) =>
              handleRatingChange(skill, event.target.value)
            }
          >
            <option value={0}>Select level</option>
            <option value={1}>1 - Beginner</option>
            <option value={2}>2 - Basic</option>
            <option value={3}>3 - Intermediate</option>
            <option value={4}>4 - Advanced</option>
            <option value={5}>5 - Expert</option>
          </select>
        </div>
      ))}
    </section>
  )
}

export default SkillAssessment