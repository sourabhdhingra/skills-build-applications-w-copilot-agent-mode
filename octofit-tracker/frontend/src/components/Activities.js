import React, { useEffect, useState } from 'react';

const Activities = () => {
  const [activities, setActivities] = useState([]);
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const apiUrl = codespace
    ? `https://${codespace}-8000.app.github.dev/api/activities/`
    : 'http://localhost:8000/api/activities/';

  useEffect(() => {
    fetch(apiUrl)
      .then(res => res.json())
      .then(data => {
        console.log('Activities API endpoint:', apiUrl);
        console.log('Fetched activities:', data);
        setActivities(data.results || data);
      });
  }, [apiUrl]);

  return (
    <div className="card mb-4">
      <div className="card-header bg-success text-white">
        <h2 className="h4">Activities</h2>
      </div>
      <div className="card-body">
        <table className="table table-striped table-bordered">
          <thead className="table-success">
            <tr>
              <th>Type</th>
              <th>Duration (min)</th>
              <th>Date</th>
              <th>User</th>
            </tr>
          </thead>
          <tbody>
            {activities.map((activity, idx) => (
              <tr key={idx}>
                <td>{activity.type}</td>
                <td>{activity.duration}</td>
                <td>{activity.date}</td>
                <td>{activity.user?.name || activity.user}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
};

export default Activities;
