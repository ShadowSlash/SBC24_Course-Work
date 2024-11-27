import React, { useState } from 'react';

const BlogDetails = ({ blog, updateBlog, clearDetails }) => {
  const [editMode, setEditMode] = useState(false);
  const [updatedTitle, setUpdatedTitle] = useState(blog.title);
  const [updatedText, setUpdatedText] = useState(blog.text);

  const handleUpdate = () => {
    updateBlog(blog.id, { title: updatedTitle, text: updatedText });
    setEditMode(false);
  };

  return (
    <div>
      <h2>Blog Details</h2>
      {editMode ? (
        <div>
          <label>Title:</label>
          <input value={updatedTitle} onChange={(e) => setUpdatedTitle(e.target.value)} />
          <label>Content:</label>
          <textarea value={updatedText} onChange={(e) => setUpdatedText(e.target.value)} />
          <button onClick={handleUpdate}>Save</button>
        </div>
      ) : (
        <div>
          <h3>{blog.title}</h3>
          <p>{blog.text}</p>
          <button onClick={() => setEditMode(true)}>Edit</button>
        </div>
      )}
      <button onClick={clearDetails}>Close</button>
    </div>
  );
};

export default BlogDetails;
