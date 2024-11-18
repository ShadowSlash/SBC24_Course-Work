import { useEffect, useState } from 'react';
import './App.css';
import BusinessCard from './components/BusinessCard';

// Import contacts from JSON file
import contacts from './data/contacts.json';

function App() {
  const [contactList, setContactList] = useState(contacts);
  const [filteredContacts, setFilteredContacts] = useState(contacts);
  const [newContact, setNewContact] = useState({
    name: '',
    position: '',
    company: '',
    email: '',
    phone: '',
    website: ''
  });
  
  const [errors, setErrors] = useState({});
  const [showErrors, setShowErrors] = useState(true);
  const [searchQuery, setSearchQuery] = useState("");

  useEffect(() => {
    console.log('This loads only once on component mount');
  }, []);

  useEffect(() => {
    console.log('This loads every time the contactList changes');
  }, [contactList]);

  useEffect(() => {
    setFilteredContacts(
      contactList.filter(contact =>
        contact.name.toLowerCase().includes(searchQuery.toLowerCase())
      )
    );
  }, [searchQuery, contactList]);
  // Validation Implement form validation
  const validate = () => {
    let tempErrors = {};
    tempErrors.name = newContact.name ? "" : "Name is required.";
    tempErrors.position = newContact.position ? "" : "Position is required.";
    tempErrors.company = newContact.company ? "" : "Company is required.";
    tempErrors.email = (/^$|.+@.+..+/).test(newContact.email) ? "" : "Email is not valid.";
    tempErrors.phone = newContact.phone ? "" : "Phone number is required.";
    tempErrors.website = newContact.website ? "" : "Website is required.";
    setErrors(tempErrors);
    setShowErrors(true);

    // Set a timer to clear errors after 5 seconds
    setTimeout(() => {
      setShowErrors(false);
    }, 5000);

    return Object.values(tempErrors).every(x => x === "");
  };

  const onSort = (sortType) => {
    const sorted = [...contactList].sort((a, b) => a[sortType].localeCompare(b[sortType]));
    setContactList(sorted);
  };

  const onAddContact = (e) => {
    e.preventDefault();
    if (validate()) {
      const newContactList = [...contactList, newContact];
      setContactList(newContactList);
      setNewContact({
        name: '',
        position: '',
        company: '',
        email: '',
        phone: '',
        website: ''
      });
      setErrors({});
    }
  };

  const onFieldChange = (e) => {
    setNewContact({
      ...newContact,
      [e.target.id]: e.target.value
    });
  };
  // Implement a search bar that filters the contacts by name
  const onSearchChange = (e) => {
    setSearchQuery(e.target.value);
  };

  return (
    <div className="app">
      <div className="search-container">
        <input
          type="text"
          placeholder="Search Contacts"
          value={searchQuery}
          onChange={onSearchChange}
        />
      </div>
      <div className="new-contact-container">
        <h2>Add a new contact</h2>
        <form onSubmit={onAddContact}>
          <input type="text" placeholder="Name" id="name" value={newContact.name} onChange={onFieldChange} />
          {showErrors && errors.name && <span>{errors.name}</span>}
          <input type="text" placeholder="Position" id="position" value={newContact.position} onChange={onFieldChange} />
          {showErrors && errors.position && <span>{errors.position}</span>}
          <input type="text" placeholder="Company" id="company" value={newContact.company} onChange={onFieldChange} />
          {showErrors && errors.company && <span>{errors.company}</span>}
          <input type="text" placeholder="Email" id="email" value={newContact.email} onChange={onFieldChange} />
          {showErrors && errors.email && <span>{errors.email}</span>}
          <input type="text" placeholder="Phone" id="phone" value={newContact.phone} onChange={onFieldChange} />
          {showErrors && errors.phone && <span>{errors.phone}</span>}
          <input type="text" placeholder="Website" id="website" value={newContact.website} onChange={onFieldChange} />
          {showErrors && errors.website && <span>{errors.website}</span>}
          <button type="submit">Add Contact</button>
        </form>
        <div className="button-container">
          <button onClick={() => onSort('name')}>Sort by Name</button>
          <button onClick={() => onSort('position')}>Sort by position</button>
        </div>
      </div>
      <div className="card-container">
        {filteredContacts.map((contact, index) => (
          <BusinessCard key={index} contact={contact} />
        ))}
      </div>
    </div>
  );
}

export default App;
