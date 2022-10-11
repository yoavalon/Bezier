d = DslBezier()

d.position_pen(1,2)
d.curve(Direction.NW, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.S, Length.long)
d.position_pen(1,1)
d.straight_line(Direction.SW, Length.medium)

d.end()
