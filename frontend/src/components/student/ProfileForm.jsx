function ProfileForm({ profile, onChange, onSubmit }) {
  const handleChange = (event) => {
    const { name, value } = event.target

    onChange({
      ...profile,
      [name]: value,
    })
  }

  return (
    <form onSubmit={onSubmit}>
      <div>
        <label htmlFor="name">Full Name</label>
        <input
          id="name"
          name="name"
          type="text"
          value={profile.name}
          onChange={handleChange}
          required
        />
      </div>

      <div>
        <label htmlFor="email">Email</label>
        <input
          id="email"
          name="email"
          type="email"
          value={profile.email}
          onChange={handleChange}
          required
        />
      </div>

      <div>
        <label htmlFor="phone">Phone</label>
        <input
          id="phone"
          name="phone"
          type="tel"
          value={profile.phone}
          onChange={handleChange}
        />
      </div>

      <div>
        <label htmlFor="institution">Institution</label>
        <input
          id="institution"
          name="institution"
          type="text"
          value={profile.institution}
          onChange={handleChange}
        />
      </div>

      <div>
        <label htmlFor="course">Course / Branch</label>
        <input
          id="course"
          name="course"
          type="text"
          value={profile.course}
          onChange={handleChange}
        />
      </div>

      <div>
        <label htmlFor="graduationYear">Graduation Year</label>
        <input
          id="graduationYear"
          name="graduationYear"
          type="number"
          value={profile.graduationYear}
          onChange={handleChange}
        />
      </div>

      <div>
        <label htmlFor="careerInterest">Career Interest</label>
        <input
          id="careerInterest"
          name="careerInterest"
          type="text"
          value={profile.careerInterest}
          onChange={handleChange}
          placeholder="e.g. Full Stack Developer"
        />
      </div>

      <button type="submit">Save Profile</button>
    </form>
  )
}

export default ProfileForm