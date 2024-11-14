import React from 'react';

const Student = ({ name, age, onClickStudent }) => {
  return (
    <li>
      {name} - {age} |
      {age > 21 && <span style={{ color: 'orange', fontWeight: 'bold' }}> Mature Student</span>}
      {age < 21 && <span style={{ color: 'green', fontWeight: 'bold' }}> Young Student</span>}
      <div>
        <button onClick={() => onClickStudent(name)}>Select</button>
      </div>
    </li>
  );
};

export default Student;
