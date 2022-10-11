d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.W, Length.medium)
d.curve(Direction.SE, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.W, Length.medium)
d.position_pen(1,1)
d.curve(Direction.NE, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.long, Radius.high)
d.straight_line(Direction.W, Length.medium)
d.straight_line(Direction.E, Length.medium)

d.end()
