import requests
from bs4 import BeautifulSoup

def fetch_google_doc(url):
    response = requests.get(url)
    if response.status_code == 200:
        print("Document fetched successfully")
        return response.text
    else:
        raise Exception("Failed to fetch document")

def parse_document(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.find('table')

    if not table:
        print("No table found in the document.")
        return []

    coordinates = []

    for row in table.find_all('tr')[1:]:  # Skip header row
        cells = row.find_all('td')

        if len(cells) < 3:
            continue  # Skip rows that do not have enough cells

        try:
            x = int(cells[0].text.strip())
            y = int(cells[1].text.strip())
            char = cells[2].text.strip()
            coordinates.append((x, y, char))
        except ValueError as e:
            print(f"Error parsing row: {row}")
            print(f"Exception: {e}")
            continue  # Skip rows with invalid data

    print(f"Parsed coordinates: {coordinates}")  # Debug output
    return coordinates

def create_grid(coordinates):
    if not coordinates:
        print("No coordinates to create grid.")
        return []

    try:
        # Determine the size of the grid
        max_x = max(x for x, _, _ in coordinates) + 1
        max_y = max(y for _, y, _ in coordinates) + 1
    except ValueError as e:
        print(f"Error calculating grid size: {e}")
        return []

    # Initialize grid with spaces
    grid = [[' ' for _ in range(max_x)] for _ in range(max_y)]

    # Fill grid with characters
    for x, y, char in coordinates:
        grid[y][x] = char

    print(f"Created grid: {grid}")  # Debug output
    return grid

def print_grid(grid):
    if not grid:
        print("Empty grid.")
        return

    for row in grid:
        print(''.join(row))

def main():
    url = 'https://docs.google.com/document/d/e/2PACX-1vRMx5YQlZNa3ra8dYYxmv-QIQ3YJe8tbI3kqcuC7lQiZm-CSEznKfN_HYNSpoXcZIV3Y_O3YoUB1ecq/pub'

    html = fetch_google_doc(url)
    coordinates = parse_document(html)
    grid = create_grid(coordinates)
    print_grid(grid)

if __name__ == "__main__":
    main()
