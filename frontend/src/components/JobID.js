import React from 'react';
import './styles.css';

const JobID = ({value, onChange}) => {
    return (
        <label className='label'>
          Job ID
          <input
          type = "text"
          value = {value}
          onChange = {onChange}
          />
        </label>
    );
};

export default JobID;
