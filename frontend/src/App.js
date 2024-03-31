import logo from './logo.svg';
import './App.css';
import React, {useState} from 'react';
import axios from 'axios';

import Date from './components/Date.js';
import Address from './components/Address.js';
import

function App() {
  const [date, setDate] = useState('');
  const [address, setAddress] = useState('');
  const [organizationName, setOrganizationName] = useState('');
  const [teamName, setTeamName] = useState('');
  const [duties, setDuties] = useState('');
  const [type, setType] = useState('techincal');

  const handleGenerate = async () => {
    const requestBody = {
      date: date,
      address: address,
      organizationName: organizationName,
      teamName: teamName,
      duties: duties,
      type: type
    };
    console.log(requestBody);
    try {
      const response = await axios.post('/generate', requestBody);
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
          checked = {type === "techincal"}
          onChange = {() => setType('technical')}
          />
          Technical
        </label>
        <label>
          <input
          type = "radio"
          value = "nonTechincal"
          checked = {type === "nonTechincal"}
          onChange = {() => setType('nonTechnical')}
          />
          Non Technical
        </label>
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
      <div>]

      </div>
      <button onClick = {handleGenerate}>Generate</button>
    </div>
  )
}

export default App;
