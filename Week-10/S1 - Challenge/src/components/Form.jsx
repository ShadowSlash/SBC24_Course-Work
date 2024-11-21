import React, { useState } from 'react';
import './Form.css';

function Form() {
  const [formData, setFormData] = useState({
    name: '',
    email: '',
    message: '',
    hearAbout: '',
    specify: ''
  });

  const [errors, setErrors] = useState({});

  const handleChange = (e) => {
    const { name, value } = e.target;
    setFormData({
      ...formData,
      [name]: value
    });
  };

  const validate = () => {
    const newErrors = {};
    if (!formData.name) newErrors.name = 'Name is required';
    if (!formData.email) newErrors.email = 'Email is required';
    if (!formData.message) newErrors.message = 'Message is required';
    if (!formData.hearAbout) newErrors.hearAbout = 'Please select an option';
    if (formData.hearAbout === 'Other' && !formData.specify) newErrors.specify = 'Please specify';
    return newErrors;
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    const validationErrors = validate();
    if (Object.keys(validationErrors).length > 0) {
      setErrors(validationErrors);
    } else {
      alert(`Form submitted:\nName: ${formData.name}\nEmail: ${formData.email}\nMessage: ${formData.message}\nHeard about us: ${formData.hearAbout} ${formData.hearAbout === 'Other' ? '- ' + formData.specify : ''}`);
      setFormData({ name: '', email: '', message: '', hearAbout: '', specify: '' });
      setErrors({});
    }
  };

  return (
    <div className="form-container">
      <h2>Contact Us</h2>
      <form onSubmit={handleSubmit}>
        <div className="form-group">
          <label>
            Name:
            <input
              type="text"
              name="name"
              value={formData.name}
              onChange={handleChange}
            />
          </label>
          {errors.name && <p className="error">{errors.name}</p>}
        </div>
        <div className="form-group">
          <label>
            Email:
            <input
              type="email"
              name="email"
              value={formData.email}
              onChange={handleChange}
            />
          </label>
          {errors.email && <p className="error">{errors.email}</p>}
        </div>
        <div className="form-group">
          <label>
            Message:
            <textarea
              name="message"
              value={formData.message}
              onChange={handleChange}
            />
          </label>
          {errors.message && <p className="error">{errors.message}</p>}
        </div>
        <div className="form-group">
          <label>
            How did you hear of us:
            <select name="hearAbout" value={formData.hearAbout} onChange={handleChange}>
              <option value="">Select</option>
              <option value="Search Engine">Search Engine</option>
              <option value="Social Media">Social Media</option>
              <option value="Word of mouth">Word of mouth</option>
              <option value="Other">Other</option>
            </select>
          </label>
          {errors.hearAbout && <p className="error">{errors.hearAbout}</p>}
        </div>
        {formData.hearAbout === 'Other' && (
          <div className="form-group">
            <label>
              Please specify:
              <input
                type="text"
                name="specify"
                value={formData.specify}
                onChange={handleChange}
              />
            </label>
            {errors.specify && <p className="error">{errors.specify}</p>}
          </div>
        )}
        <button type="submit" className="submit-button">Submit</button>
      </form>
    </div>
  );
}

export default Form;