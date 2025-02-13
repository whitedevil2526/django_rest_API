import React from 'react'; // Make sure to import React
import Todo from './components/todo.jsx'; // Corrected import path (case-sensitive)

function App() {
  return ( // Use parentheses instead of curly braces for JSX
    <div className="App">
      <Todo/>
    </div>
  );
}

export default App; // No parentheses here, just export the component