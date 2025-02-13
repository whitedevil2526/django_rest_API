import React, { useState, useEffect } from 'react';
import axios from 'axios';
import './todo.css';
const Todo = () => {
    const [todos, setTodos] = useState([]);
    const [newTodo, setNewTodo] = useState({ title: '', description: '' });

    // Fetch todos on component mount
    useEffect(() => {
        fetchTodos();
    }, []);

    // Fetch todos from the API
    const fetchTodos = async () => {
        try {
            const response = await axios.get('http://127.0.0.1:8000/todos/');
            setTodos(response.data);
        } catch (error) {
            console.error('Error fetching todos:', error);
        }
    };

    // Add a new todo
    const addTodo = async () => {
        console.log('New Todo:', newTodo); // Log the newTodo state
        if (!newTodo.title || !newTodo.description) {
            alert('Please fill in both title and description');
            return;
        }
        try {
            const response = await axios.post('http://127.0.0.1:8000/todos/', newTodo);
            console.log('Response:', response.data); // Log the response
            setNewTodo({ title: '', description: '' }); // Clear the input fields
            fetchTodos(); // Refresh the list
        } catch (error) {
            console.error('Error adding todo:', error);
            if (error.response) {
                // The request was made and the server responded with a status code
                console.error('Response data:', error.response.data);
                console.error('Response status:', error.response.status);
                console.error('Response headers:', error.response.headers);
            } else if (error.request) {
                // The request was made but no response was received
                console.error('Request:', error.request);
            } else {
                // Something happened in setting up the request that triggered an Error
                console.error('Error message:', error.message);
            }
        }
    };

    // Delete a todo
    const deleteTodo = async (id) => {
        try {
            await axios.delete(`http://127.0.0.1:8000/todos/${id}/`);
            fetchTodos(); // Refresh the list
        } catch (error) {
            console.error('Error deleting todo:', error);
        }
    };

    return (
        <div>
            <h1>Todo App</h1>
            <div>
                <input
                    type="text"
                    placeholder="Title"
                    value={newTodo.title}
                    onChange={(e) => setNewTodo({ ...newTodo, title: e.target.value })}
                />
                <input
                    type="text"
                    placeholder="Description"
                    value={newTodo.description}
                    onChange={(e) => setNewTodo({ ...newTodo, description: e.target.value })}
                />
                <button onClick={addTodo}>Add Todo</button>
            </div>
            <ul>
                {todos.map((todo) => (
                    <li key={todo.id}>
                        <h2>{todo.title}</h2>
                        <p>{todo.description}</p>
                        <button onClick={() => deleteTodo(todo.id)}>Delete</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Todo;