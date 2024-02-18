export default function getNeighborhoodsList() {
    this.sanFranciscoNeighborhoods = ['SOMA', 'union Square'];

    const self = this;
    this.addNeighborhood = (newNeighborhood) => {
        self.sanFranciscoNeighborhoods.push(newNeighborhood);
        return self.sanFranciscoNeighborhoods;
    };
}
