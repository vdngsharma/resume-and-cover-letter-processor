import React from 'react';

const OrganizationName = ({value, onChange}) => {
    return (
        <label className='label'>
          Organization Name:
          <input
          type = "text"
          value = {value}
          onChange = {onChange}
          />
        </label>
    );
};

export default OrganizationName;
