require 'MetaData2'


meta_object do
  extend MetaData2

  def remote_directory
    Pathname.new '/var/www/courses/scripting'
  end
end
