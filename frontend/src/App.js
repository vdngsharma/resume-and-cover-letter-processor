import './App.css';
import React, {useState} from 'react';
import axios from 'axios';

import JobID from './components/JobID.js';
import Date from './components/Date.js';
import Address from './components/Address.js';
import JobTitle from './components/JobTitle.js'
import OrganizationName from './components/OrganizationName.js';
import TeamName from './components/TeamName.js';
import Duties from './components/Duties.js';

function App() {
  const [jobId, setJobId] = useState('');
  const [type, setType] = useState('');
  const [date, setDate] = useState('');
  const [address, setAddress] = useState('');
  const [jobTitle, setJobTitle] = useState('');
  const [organizationName, setOrganizationName] = useState('');
  const [teamName, setTeamName] = useState('');
  const [duties, setDuties] = useState('');

  const handleGenerate = async () => {
    const requestBody = {
      jobId: jobId,
      type: type,
      date: date,
      address: address,
      jobTitle: jobTitle,
      organizationName: organizationName,
      teamName: teamName,
      duties: duties
    };
    console.log(requestBody);
    try {
      const response = await axios.post('http://localhost:5000/generate', 
      requestBody,
      {
      headers: {
          'Content-Type': 'application/json',
      }});
      console.log(response.data);
    } catch(error) {
      console.error('Error while making API call:', error);
    }
  };

  return (
    <div>
        <div>
        <label>
          <input
          type = "radio"
          value = "techincal"
          checked = {type === "technical"}
          onChange = {() => setType('technical')}
          />
          Technical
        </label>
        <label>
          <input
          type = "radio"
          value = "nonTechincal"
          checked = {type === "nonTechnical"}
          onChange = {() => setType('nonTechnical')}
          />
          Non Technical
        </label>
        </div>
        <div>
          <JobID
          value = {jobId}
          onChange = {(e) => setJobId(e.target.value)}
          />
        </div>
        <div>
          <Date
          value = {date}
          onChange = {(e) => setDate(e.target.value)}
          />
        </div>
        <div>
          <Address
          value = {address}
          onChange = {(e) => setAddress(e.target.value)}
          />
        </div>
        <div>
          <JobTitle
          value = {jobTitle}
          onChange = {(e) => setJobTitle(e.target.value)}
          />
        </div>
        <div>
          <OrganizationName
          value = {organizationName}
          onChange = {(e) => setOrganizationName(e.target.value)}
          />
        </div>
        <div>
          <TeamName
          value = {teamName}
          onChange = {(e) => setTeamName(e.target.value)}
          />
        </div>
        <div>
          <Duties
          value = {duties}
          onChange = {(e) => setDuties(e.target.value)}
          />
        </div>
      <div>
      </div>
      <button onClick = {handleGenerate}>Generate</button>
    </div>
  )
}

export default App;
