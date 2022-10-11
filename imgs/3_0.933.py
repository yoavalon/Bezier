d = DslBezier()

d.position_pen(1,0)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.SW, Length.long)
d.curve(Direction.N, Orient.right, Length.medium, Radius.medium)
d.position_pen(1,2)

d.end()
