import { Box, Paper, Typography } from '@mui/material'
import { deepPurple, purple } from '@mui/material/colors'
import React from 'react'
import poza from '../components/photos/stapanulinelelor.jpg'
import Recenzie from '../components/Recenzie'
import Link from '@mui/material/Link';
import back from "../components/photos/back.jpg"


const StapanulInelelor = () => {
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
        <Typography fontSize={60} paddingTop={'5px'}>Stăpânul Inelelor</Typography>
        <Typography fontSize={25} paddingBottom={'2px'}>de J.R.R. Tolkien</Typography>
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
            <Typography fontSize={'18px'} color={'white'}>"Stăpânul Inelelor" este o trilogie epică scrisă de J.R.R. 
            Tolkien, care urmărește aventurile unui grup de eroi într-o lume fantastică numită Pământul de Mijloc. 
            Povestea începe cu apariția unui inel puternic și malefic, iar destinul său devine centrul conflictului 
            care amenință să distrugă lumea. Eroul principal, Frodo Baggins, este însărcinat cu misiunea de a distruge 
            inelul în Muntele Doom, singurul loc în care poate fi distrus, însoțit de o echipă variată de personaje. 
            "Stăpânul Inelelor" explorează teme precum curajul, prietenia și lupta împotriva răului, devenind o operă
            emblematică în literatura fantasy.
            </Typography>
            </Box>
        </Box>
        <Box sx={{
            paddingY: '20px'
        }}>
            <Link underline='hover' color={purple[800]} fontSize={30} href={'https://www.docdroid.net/V2W701D/tolkien-stapinul-inelelor-1-fratia-inelului-pdf'}
            >Citește cartea aici</Link>
        </Box>
        <Typography fontSize={25}>Acum că ai citit cartea, acordă-i o recenzie!</Typography>
        <Recenzie/>
    </Box>
  )
}

export default StapanulInelelor