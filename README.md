# Data Center Locations Visualization

This project visualizes the locations of AWS, Azure, and custom data centers on a world map using Python and Folium.

## Table of Contents

- [Overview](#overview)
- [Data Center Locations](#data-center-locations)
  - [AWS Locations](#aws-locations)
  - [Azure Locations](#azure-locations)
  - [Custom Locations](#custom-locations)
- [Setup](#setup)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project provides a visual representation of data center locations for AWS, Azure, and additional custom locations. The map markers are color-coded for easy distinction:
- **Orange**: AWS Data Centers
- **Blue**: Azure Data Centers
- **Pink**: Custom Locations

## Data Center Locations

### AWS Locations

The following AWS data centers are visualized:

- Northern Virginia, USA
- Ohio, USA
- Northern California, USA
- Oregon, USA
- Montréal, Canada
- São Paulo, Brazil
- Ireland, Ireland
- Frankfurt, Germany
- London, UK
- Paris, France
- Stockholm, Sweden
- Milan, Italy
- Cape Town, South Africa
- Bahrain, Bahrain
- Singapore, Singapore
- Tokyo, Japan
- Osaka, Japan
- Seoul, South Korea
- Mumbai, India
- Sydney, Australia
- Melbourne, Australia
- Jakarta, Indonesia
- Hong Kong, Hong Kong
- Hyderabad, India
- Beijing, China
- Ningxia, China

### Azure Locations

The following Azure data centers are visualized:

- Central US, USA
- East US, USA
- East US 2, USA
- North Central US, USA
- South Central US, USA
- West US, USA
- West US 2, USA
- Canada Central, Canada
- Brazil South, Brazil
- North Europe, Ireland
- West Europe, Netherlands
- UK South, UK
- UK West, UK
- France Central, France
- Germany West Central, Germany
- Switzerland North, Switzerland
- Switzerland West, Switzerland
- Norway East, Norway
- Norway West, Norway
- Japan East, Japan
- Japan West, Japan
- Korea Central, South Korea
- Korea South, South Korea
- Australia East, Australia
- Australia Southeast, Australia
- East Asia, Hong Kong
- Southeast Asia, Singapore
- India Central, India
- India South, India
- India West, India
- China East, China
- China North, China
- UAE North, UAE
- South Africa North, South Africa

### Custom Locations

The following custom locations are visualized:

- Tromsø, Norway


## Setup

### Prerequisites

- Python 3.6+
- Pip (Python package installer)
- Virtual environment (optional but recommended)

### Installation

1. Clone the repository:

```
git clone https://github.com/yourusername/datacenter-visualization.git
cd datacenter-visualization
```

2. Create and activate a virtual environment:

```
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. Install the required packages:

```
pip install folium
```

## Usage

1. Run the Python script:

```
python main.py
```

2. Open the generated `data_centers_map.html` file in your web browser to view the map.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
