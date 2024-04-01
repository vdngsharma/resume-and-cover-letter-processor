import React from 'react';

const TeamName = ({value, onChange}) => {
    return (
        <label className='label'>
          Team Name:
          <input
          type = "text"
          value = {value}
          onChange = {onChange}
          />
        </label>
    );
};

export default TeamName;
