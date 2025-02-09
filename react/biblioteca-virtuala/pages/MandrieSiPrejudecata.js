import { Box, Paper, Typography } from '@mui/material'
import { deepPurple, purple } from '@mui/material/colors'
import React from 'react'
import poza from '../components/photos/mandriesiprejudecata.jpeg'
import Recenzie from '../components/Recenzie'
import Link from '@mui/material/Link';
import back from "../components/photos/back.jpg"


const MandrieSiPrejudecata = () => {
  return (
    <Box sx={{
        width: "100vw",
        height: "100%",
        display: "flex",
        flexDirection: "column",
        alignItems: "center",
        alignSelf: "center",
        //gap: 1,
        borderRadius: "2px",
        backgroundImage: `url(${back})`,
        backgroundRepeat: 'no-repeat',
        backgroundSize: 'cover',
        opacity: 0.95
      }}>
        <Typography fontSize={60} paddingTop={'5px'}>Mândrie și prejudecată</Typography>
        <Typography fontSize={25} paddingBottom={'2px'}>de Jane Austen</Typography>
        <Box sx={{
            width: "90vw",
            height: "90vh",
            display: "flex",
            flexDirection: "row",
            alignItems: "center",
            alignSelf: "center",
            }}>
            <Paper
                elevation={7}
                component="form"
                sx={{
                    width: '370px',
                    height: '440px',
                    alignSelf: "center",
                    p: 2,
                    gap: 1,
                    borderRadius: "5px",
                    backgroundImage: `url(${poza})`,
                    margin: '70px',
                    marginRight: '150px',
                    backgroundRepeat: 'no-repeat',
                    backgroundSize: '320px'
                }}
            ></Paper>

            <Box sx={{
            width: "1000px",
            maxHeight: "300px",
            display: "flex",
            flexDirection: "column",
            backgroundColor: purple[800],
            padding: '35px',
            borderRadius: '7px'
            }}>
            <Typography fontSize={'18px'} color={'white'}>"Mândrie și prejudecată" este un roman clasic scris de Jane 
            Austen, care urmărește povestea familiei Bennet din secolul al XIX-lea din Anglia rurală. Povestea se 
            concentrează pe viața celor cinci fiice ale familiei Bennet și pe încercările lor de a-și găsi un partener 
            potrivit într-o societate dominată de convenții și norme sociale stricte. Eroul principal, Elizabeth Bennet, 
            este o tânără inteligentă și independentă, care se îndrăgostește de Mr. Darcy, un bărbat bogat și mândru, dar 
            cu inimă nobilă. Romanul explorează teme precum iubirea, mândria, prejudecățile sociale și condiția femeii în 
            societatea vremii. Este una dintre cele mai iubite și citite opere ale literaturii engleze și a avut un 
            impact durabil asupra culturii populare.
            </Typography>
            </Box>
        </Box>
        <Box sx={{
            paddingY: '20px'
        }}>
            <Link underline='hover' color={purple[800]} fontSize={30} href={'https://dn790002.ca.archive.org/0/items/LiteraturaUniversala-Mix001/Jane%20Austen%20-%20Mandrie%20si%20prejudecata.pdf'}
            >Citește cartea aici</Link>
        </Box>
        <Typography fontSize={25}>Acum că ai citit cartea, acordă-i o recenzie!</Typography>
        <Recenzie/>
    </Box>
  )
}

export default MandrieSiPrejudecata