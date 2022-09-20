d = DslBezier()

d.position_pen(1,2)
d.straight_line(Direction.NW, Length.medium)
d.straight_line(Direction.NE, Length.medium)
d.position_pen(1,3)
d.curve(Direction.S, Orient.right, Length.medium, Radius.high)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.high)
d.straight_line(Direction.SW, Length.medium)

d.end()
