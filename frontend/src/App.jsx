import { useState } from 'react'
import SkillAssessment from './components/student/SkillAssessment'

function App() {
  const [currentPage, setCurrentPage] = useState('dashboard')

  return (
    <>
      <nav>
        <h1>SkillSync</h1>

        <button
          type="button"
          onClick={() => setCurrentPage('dashboard')}
        >
          Student Dashboard
        </button>

        <button
          type="button"
          onClick={() => setCurrentPage('skills')}
        >
          Skill Assessment
        </button>
      </nav>

      {currentPage === 'dashboard' && (
        <main>
          <h2>Student Dashboard</h2>
          <p>Welcome to your SkillSync student dashboard.</p>

          <button
            type="button"
            onClick={() => setCurrentPage('skills')}
          >
            Open Skill Assessment
          </button>
        </main>
      )}

      {currentPage === 'skills' && <SkillAssessment />}
    </>
  )
}

export default App