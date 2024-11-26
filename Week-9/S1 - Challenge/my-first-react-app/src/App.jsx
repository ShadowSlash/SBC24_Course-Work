import { useState } from "react";
import "./App.css";
import Student from "./components/Students";

function App() {
  const students = [
    { name: "Leo", age: 25 },
    { name: "Vitor", age: 18 },
    { name: "Matt", age: 22 },
    { name: "Susie", age: 20 },
    { name: "Eoghan", age: 23 },
  ];

  const [count, setCount] = useState(1);
  const [selectedStudent, setSelectedStudent] = useState("");

  const handleClick = () => {
    if (count < students.length) {
      setCount(count + 1);
    }
  };

  const onClickStudent = (studentName) => {
    setSelectedStudent(studentName);
  };

  return (
    <div>
      <h1>Student Names</h1>
      <ul>
        {students.slice(0, count).map((student, index) => (
          <Student
            key={index}
            name={student.name}
            age={student.age}
            onClickStudent={onClickStudent}
          />
        ))}
      </ul>
      <button onClick={handleClick}>Show Next Student</button>
      {selectedStudent && <p>Selected Student: {selectedStudent}</p>}
    </div>
  );
}

export default App;

// import reactLogo from './assets/react.svg'
// import viteLogo from '/vite.svg'

// function App() {
//   const [count, setCount] = useState(0)

//   return (
//     <>
//       <div>
//         <a href="https://vite.dev" target="_blank">
//           <img src={viteLogo} className="logo" alt="Vite logo" />
//         </a>
//         <a href="https://react.dev" target="_blank">
//           <img src={reactLogo} className="logo react" alt="React logo" />
//         </a>
//       </div>
//       <h1>Vite + React</h1>
//       <div className="card">
//         <button onClick={() => setCount((count) => count + 1)}>
//           count is {count}
//         </button>
//         <p>
//           Edit <code>src/App.jsx</code> and save to test HMR
//         </p>
//       </div>
//       <p className="read-the-docs">
//         Click on the Vite and React logos to learn more
//       </p>
//     </>
//   )
// }

// export default App

// src/App.jsx
