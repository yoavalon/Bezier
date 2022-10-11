d = DslBezier()

d.position_pen(2,0)
d.straight_line(Direction.SW, Length.medium)
d.position_pen(2,1)
d.straight_line(Direction.N, Length.medium)
d.curve(Direction.SW, Orient.right, Length.medium, Radius.low)
d.position_pen(1,0)
d.straight_line(Direction.SW, Length.long)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)

d.end()
