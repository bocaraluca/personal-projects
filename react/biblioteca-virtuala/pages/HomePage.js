import React from 'react';
import { Box } from '@mui/material';
import back from '../components/photos/back.jpg';
import InfoForm from '../components/InfoForm';

const HomePage = () => {
  return (
    <Box sx={{
      display: 'flex',
      flexWrap:'wrap',
      flexDirection:'column',
      justifyContent:'center',
      backgroundImage: `url(${back})`,
      backgroundRepeat: 'no-repeat',
      backgroundSize: 'cover',
      opacity: 0.95,
      gap: '10px',
      padding: '50px',
      alignItems: 'center'
    }}>
      <InfoForm/>
    </Box>
  );
}

export default HomePage;