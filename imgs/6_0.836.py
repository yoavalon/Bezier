d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.SW, Length.long)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.high)
d.curve(Direction.NE, Orient.left, Length.long, Radius.medium)
d.position_pen(1,3)

d.end()
