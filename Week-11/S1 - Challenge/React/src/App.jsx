import React, { useState, useEffect } from "react";
import BlogList from "./components/BlogList";
import BlogForm from "./components/BlogForm";
import BlogDetails from "./components/BlogDetails";
import styles from "./App.module.css";

const App = () => {
  const [blogs, setBlogs] = useState([]);
  const [selectedBlog, setSelectedBlog] = useState(null);

  // Fetch all blogs
  const fetchBlogs = async () => {
    const response = await fetch("http://127.0.0.1:8000/blog/");
    const data = await response.json();
    setBlogs(data.data);
  };

  useEffect(() => {
    fetchBlogs();
  }, []);

  const addBlog = async (blog) => {
    await fetch("http://127.0.0.1:8000/blog/add/", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(blog),
    });
    fetchBlogs();
  };

  const deleteBlog = async (id) => {
    await fetch(`http://127.0.0.1:8000/blog/delete/${id}`, {
      method: "DELETE",
    });

    fetchBlogs();
  };

  const updateBlog = async (id, updatedBlog) => {
    await fetch(`http://127.0.0.1:8000/blog/update/${id}`, {
      method: "PUT",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(updatedBlog),
    });

    fetchBlogs();
  };

  const fetchBlogDetails = async (id) => {
    const response = await fetch(`http://127.0.0.1:8000/blog/get/${id}/`);
    const data = await response.json();
    setSelectedBlog(data);
  };

  return (
    <div className={styles.container}>
      <h1 className={styles.header}>Blog Manager</h1>
      <div className={styles.formSection}>
        <BlogForm addBlog={addBlog} />
      </div>
      <div className={styles.blogSection}>
        <BlogList
          blogs={blogs}
          deleteBlog={deleteBlog}
          fetchBlogDetails={fetchBlogDetails}
        />
        {selectedBlog && (
          <BlogDetails
            blog={selectedBlog}
            updateBlog={updateBlog}
            clearDetails={() => setSelectedBlog(null)}
          />
        )}
      </div>
    </div>
  );
};

export default App;
