import React from 'react';
import PropTypes from 'prop-types';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import Paper from '@material-ui/core/Paper';
import Link from '@material-ui/core/Link';
import '../homePage/tables.css';
import HighlightOffIcon from '@material-ui/icons/HighlightOff';

const LeagueTable = ({
  table,
  openLeague,
}) => {
  return (
    <TableContainer component={Paper} className='tableContainer'>
      <h1 className='h1'>My Leagues</h1>
      <Table aria-label="customized table">
        <TableHead>
          <TableRow>
            <TableCell height="auto" align="center">League ID</TableCell>
            <TableCell align="center" >Status</TableCell>
            <TableCell align="center" >Pick</TableCell>
          </TableRow>
        </TableHead>
        <TableBody style={{minHeight: 'auto'}}>
          {table.map((item) => (
            <TableRow key={item[0]['LeagueID']}>
              <TableCell align='center'>
                {/* eslint-disable-next-line max-len */}
                <Link className='tableLink' onClick={() => openLeague(item[0]['LeagueID'])}>{item[0]['LeagueID']}</Link>
              </TableCell>
              {(item[0]['Status'] === 'In') ? (
                <TableCell align="center" >
                  {/* eslint-disable-next-line max-len */}
                  <img src={require('../../images/leagueStatusIn.png')} alt="logo" width="20px"></img>
                </TableCell>
                  ) : (
                  <TableCell align="center"><HighlightOffIcon/></TableCell>
                )}
              <TableCell align="center">{item[0]['CurrentPick']}</TableCell>
            </TableRow>))}
        </TableBody>
      </Table>
    </TableContainer>
  );
};

LeagueTable.propTypes = {
  table: PropTypes.object,
  openLeague: PropTypes.func.isRequired,
};

LeagueTable.defaultProps = {
  table: {},
};

export default LeagueTable;
