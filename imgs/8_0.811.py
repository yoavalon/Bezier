d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.S, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.NW, Length.long)

d.end()
