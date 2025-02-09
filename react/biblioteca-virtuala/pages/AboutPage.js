import { Box } from '@mui/material'
import back from '../components/photos/back.jpg'
import React from 'react'
import AboutForm from '../components/AboutForm'

const AboutPage = () => {
  return (
    <Box sx={{
      width: "100vw",
      height: "100vh",
      backgroundImage: `url(${back})`,
      backgroundRepeat: 'no-repeat',
      backgroundSize: 'cover',
      opacity: 0.95,
      alignItems: 'center',
      padding: '5px',
      display: 'flex',
      flexDirection: 'row',
    }}>
      <AboutForm/>

    </Box>
  )
}

export default AboutPage