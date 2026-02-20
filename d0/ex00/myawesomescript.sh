url="$1"
redirected=$(curl -s -o /dev/null -w "%{redirect_url}" "$url")
echo "$redirected"