import React from 'react';

const JobTitle = ({value, onChange}) => {
    return (
        <label>
          Job Title:
          <input
          type = "text"
          value = {value}
          onChange = {onChange}
          />
        </label>
    );
};

export default JobTitle;
