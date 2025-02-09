import { Button, Typography } from '@mui/material'
import React from 'react'
import { Link } from 'react-router-dom'

const Card = (props) => {
  return (
    <div sx={{
      minWidth: '700px',
      height: '500px',
      maxHeight: '500px',
      margin: '20px',
      padding: '30px',
      borderRadius: '10px',
      display: 'flex',
      flexDirection: 'column',
    }}>
      <Typography fontSize={30} align='center' >{props.titlu}</Typography>
      <img src={props.src} alt={props.titlu}/>
      <p >{props.autor}</p>
      <Link
        to={props.link} style={{textTransform:"none", textDecoration:"none", color:"inherit"}}
      ><Button>Vezi mai multe informații</Button>
      </Link>
    </div>
  )
}

export default Card