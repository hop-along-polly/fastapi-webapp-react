import { render, screen } from '@testing-library/react';
import { MemoryRouter } from 'react-router-dom';
import App from './App';

describe('App', () => {
  it('renders the home route', () => {
    render(
      <MemoryRouter initialEntries={['/']}>
        <App />
      </MemoryRouter>,
    );
    expect(screen.getByText('Home')).toBeInTheDocument();
  });

  it('renders the test route', () => {
    render(
      <MemoryRouter initialEntries={['/test']}>
        <App />
      </MemoryRouter>,
    );
    expect(screen.getByText('Test')).toBeInTheDocument();
  });
});
