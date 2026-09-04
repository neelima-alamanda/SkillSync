import { useState } from 'react'
import ProfileForm from '../../components/student/ProfileForm'

const initialProfile = {
  name: '',
  email: '',
  phone: '',
  institution: '',
  course: '',
  graduationYear: '',
  careerInterest: '',
}

function StudentProfile() {
  const [profile, setProfile] = useState(initialProfile)
  const [saved, setSaved] = useState(false)

  const handleChange = (updatedProfile) => {
    setProfile(updatedProfile)
    setSaved(false)
  }

  const handleSubmit = (event) => {
    event.preventDefault()

    // Backend integration will be added after the API contract
    // is finalized with Member 4.
    setSaved(true)
  }

  return (
    <main>
      <header>
        <h1>Student Profile</h1>
        <p>
          Build your SkillSync profile to receive relevant career,
          internship, and placement recommendations.
        </p>
      </header>

      <ProfileForm
        profile={profile}
        onChange={handleChange}
        onSubmit={handleSubmit}
      />

      {saved && (
        <p role="status">
          Profile saved locally. Backend synchronization will be connected
          once the API contract is available.
        </p>
      )}
    </main>
  )
}

export default StudentProfile