import React from 'react';
import styles from './BlogList.module.css';

const BlogList = ({ blogs, deleteBlog, fetchBlogDetails }) => {
  return (
    <div className={styles.listContainer}>
      <h2>All Blogs</h2>
      <ul>
        {blogs.map((blog) => (
          <li key={blog.id} className={styles.blogCard}>
            <div>
              <strong>{blog.title}</strong>
            </div>
            <div>
              <button onClick={() => fetchBlogDetails(blog.id)}>View</button>
              <button onClick={() => deleteBlog(blog.id)} className={styles.deleteButton}>
                Delete
              </button>
            </div>
          </li>
        ))}
      </ul>
    </div>
  );
};

export default BlogList;
