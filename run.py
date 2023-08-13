import weather

if __name__ == "__main__":
    print('Welcome to Weather Forecasting App!\n')
    user_args = weather.read_user_cli_args()
    query_url = weather.build_weather_query(user_args.city, user_args.imperial)
    weather_data = weather.get_weather_data(query_url)
    weather.display_weather_info(weather_data, user_args.imperial)
