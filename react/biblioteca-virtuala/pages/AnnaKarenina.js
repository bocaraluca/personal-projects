import { Box, Paper, Typography } from '@mui/material'
import { deepPurple, purple } from '@mui/material/colors'
import React from 'react'
import poza from '../components/photos/annakarenina.jpg'
import Recenzie from '../components/Recenzie'
import Link from '@mui/material/Link';
import back from "../components/photos/back.jpg"


const AnnaKarenina = () => {
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
        <Typography fontSize={60} paddingTop={'5px'}>Anna Karenina</Typography>
        <Typography fontSize={25} paddingBottom={'2px'}>de Lev Tolstoi</Typography>
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
                    backgroundSize: 'cover'
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
            <Typography fontSize={'18px'} color={'white'}>Romanul "Anna Karenina" de Lev Tolstoi este o poveste captivantă
            despre o femeie prinsă într-o pasiune adulterină distructivă. Anna Karenina, o femeie nobilă și sofisticată, 
            se îndrăgostește de Contele Vronski și își sacrifică reputația și familia pentru această relație interzisă.
            Pe măsură ce povestea avansează, Tolstoi explorează ipocrizia și decaderea societății rusești din secolul al 
            XIX-lea. Anna și cei din jurul ei luptă cu judecățile societății și cu propria lor moralitate, iar 
            consecințele pasiunii lor sunt devastatoare. "Anna Karenina" este o operă profundă care analizează natura 
            umană, complexitatea relațiilor și costurile unei pasiuni interzise. Romanul rămâne unul dintre cele mai 
            influente din literatura mondială.
            </Typography>
            </Box>
        </Box>
        <Box sx={{
            paddingY: '20px'
        }}>
            <Link underline='hover' color={purple[800]}fontSize={30} href={'http://95.80.182.68:207/documents/10157/39107/Lev+Tolstoi-Anna+Karenina-Polirom+%282007%29.pdf'}
            >Citește cartea aici</Link>
        </Box>
        <Typography fontSize={25}>Acum că ai citit cartea, acordă-i o recenzie!</Typography>
        <Recenzie/>
    </Box>
  )
}

export default AnnaKarenina