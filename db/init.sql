CREATE TABLE IF NOT EXISTS todos (
    id SERIAL PRIMARY KEY,
    task TEXT NOT NULL,
    done BOOLEAN DEFAULT FALSE
);

-- Seed with 10 todos
INSERT INTO todos (task, done) VALUES
('Learn Docker', false),
('Set up Flask app', false),
('Integrate Postgres', false),
('Try HTMX', false),
('Write Dockerfile', false),
('Deploy to VPS', false),
('Configure Nginx', false),
('Buy domain', false),
('Connect domain to VPS', false),
('Ship Todo App!', false);
