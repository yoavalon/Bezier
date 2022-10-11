d = DslBezier()

d.position_pen(0,1)
d.curve(Direction.S, Orient.right, Length.medium, Radius.high)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(2,2)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.position_pen(2,0)
d.straight_line(Direction.S, Length.long)

d.end()
