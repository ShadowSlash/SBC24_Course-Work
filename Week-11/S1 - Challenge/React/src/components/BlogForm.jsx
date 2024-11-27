import React, { useState } from 'react';

const BlogForm = ({ addBlog }) => {
  const [title, setTitle] = useState('');
  const [text, setText] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();

    const publishDate = new Date().toISOString();

    addBlog({ 
        title: title, 
        text:text,
        published_date: publishDate,
        created_date: publishDate,
        author: 1,
    }
    );
    setTitle('');
    setText('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <h2>Add Blog</h2>
      <div>
        <label>Title:</label>
        <input type="text" value={title} onChange={(e) => setTitle(e.target.value)} required />
      </div>
      <div>
        <label>Content:</label>
        <textarea value={text} onChange={(e) => setText(e.target.value)} required />
      </div>
      <button type="submit">Add</button>
    </form>
  );
};

export default BlogForm;
