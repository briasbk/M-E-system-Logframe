import React, { useEffect, useState } from "react";
import { getHouseholds } from "../api/household";

const HouseholdList = () => {
  const [households, setHouseholds] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchHouseholds = async () => {
      try {
        const data = await getHouseholds();
        setHouseholds(data);
        setLoading(false);
      } catch (error) {
        console.error("Error fetching households:", error);
      }
    };
    fetchHouseholds();
  }, []);

  if (loading) return <p>Loading households...</p>;

  return (
    <div>
      <h1>Household List</h1>
      <ul>
        {households.map((household) => (
          <li key={household.id}>
            {household.head_of_household} - {household.location}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default HouseholdList;
