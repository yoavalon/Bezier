d = DslBezier()

d.position_pen(1,0)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.S, Length.medium)
d.position_pen(0,3)
d.position_pen(2,1)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.S, Length.medium)

d.end()
