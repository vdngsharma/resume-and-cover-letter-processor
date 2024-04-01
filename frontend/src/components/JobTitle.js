import React from 'react';
import './styles.css';

const JobTitle = ({value, onChange}) => {
    return (
      <label className='label'>
        JOB TITLE
          <input
          type = "text"
          value = {value}
          onChange = {onChange}
          />
        </label>
    );
};

export default JobTitle;
