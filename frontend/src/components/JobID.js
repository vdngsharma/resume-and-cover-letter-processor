import React from 'react';

const JobID = ({value, onChange}) => {
    return (
        <label>
          Job ID:
          <input
          type = "text"
          value = {value}
          onChange = {onChange}
          />
        </label>
    );
};

export default JobID;
