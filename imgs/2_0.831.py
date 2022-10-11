d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.high)
d.position_pen(2,2)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.NE, Length.long)

d.end()
